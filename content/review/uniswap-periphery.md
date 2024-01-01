# 🔄 Why Uniswap V2 & V3 Need a Periphery Contract

> *Assumption: The reader is already familiar with Automated Market Makers (AMM) and ERC20 tokens.*

> HackMD Link: []


## 🧩 Problem Statement

Let's consider a scenario with three AMM pools in our hypothetical DEX:

- **WETH-DAI**
- **WETH-TokenX**
- **TokenX-TokenY**

In this DEX, the Swap function utilizes the approval given to the pool to first perform `transferFrom`, and then it executes the swap.

### Scenarios

1. **User A's Scenario: Splitting WETH**
   - **Goal**: Sell all WETH, half for DAI and the other half for TokenX.
   - **Process**: 
     - Issue two separate approval transactions for WETH - one for WETH-DAI and another for WETH-TokenX.
     - Conduct two individual swap transactions.

2. **User2's Scenario: Purchasing TokenY with DAI**
   - **Goal**: Convert DAI into TokenY, passing through multiple tokens.
   - **Process**: 
     - Approve DAI for the WETH-DAI pair.
     - Swap on the WETH-DAI pair.
     - Approve WETH for the WETH-TokenX pair.
     - Swap on the WETH-TokenX pair.
     - Approve TokenX for the TokenX-TokenY pair.
     - Finally, swap on the TokenX-TokenY pair.

### Problems Identified

1. **Multiple Approvals**: Need to approve a single token multiple times for different pools on the same platform.
2. **No Routing**: The absence of a routing feature complicates the process and increases costs.

## 🛠️ Solution: Periphery Contract or "Router"

Uniswap V2 and V3 address these issues using a periphery contract, commonly referred to as a "router."

### Context

- Uniswap V2 and V3 deploy different contracts for each pair due to their factory pattern. V4, however, consolidates all pools into one contract, changing the paradigm.

### Implementation

- **Interaction Limitation**: Direct interaction with pair contracts from Externally Owned Accounts (EOAs) is impractical.
- **Operational Flow**:
  - Uniswap functions calculate user input as the difference in token balances before and after the transaction.
  - This difference is then used to adjust the reserves.

```
    // this low-level function should be called from a contract which performs important safety checks
    function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external lock {
        require(amount0Out > 0 || amount1Out > 0, 'UniswapV2: INSUFFICIENT_OUTPUT_AMOUNT');
>         (uint112 _reserve0, uint112 _reserve1,) = getReserves(); // gas savings
>         require(amount0Out < _reserve0 && amount1Out < _reserve1, 'UniswapV2: INSUFFICIENT_LIQUIDITY');

>         uint balance0;
>         uint balance1;
        { // scope for _token{0,1}, avoids stack too deep errors
        address _token0 = token0;
        address _token1 = token1;
        require(to != _token0 && to != _token1, 'UniswapV2: INVALID_TO');
        if (amount0Out > 0) _safeTransfer(_token0, to, amount0Out); // optimistically transfer tokens
        if (amount1Out > 0) _safeTransfer(_token1, to, amount1Out); // optimistically transfer tokens
        if (data.length > 0) IUniswapV2Callee(to).uniswapV2Call(msg.sender, amount0Out, amount1Out, data);
        balance0 = IERC20(_token0).balanceOf(address(this));
        balance1 = IERC20(_token1).balanceOf(address(this));
        }
>         uint amount0In = balance0 > _reserve0 - amount0Out ? balance0 - (_reserve0 - amount0Out) : 0;
>         uint amount1In = balance1 > _reserve1 - amount1Out ? balance1 - (_reserve1 - amount1Out) : 0;
        require(amount0In > 0 || amount1In > 0, 'UniswapV2: INSUFFICIENT_INPUT_AMOUNT');
        { // scope for reserve{0,1}Adjusted, avoids stack too deep errors
        uint balance0Adjusted = balance0.mul(1000).sub(amount0In.mul(3));
        uint balance1Adjusted = balance1.mul(1000).sub(amount1In.mul(3));
        require(balance0Adjusted.mul(balance1Adjusted) >= uint(_reserve0).mul(_reserve1).mul(1000**2), 'UniswapV2: K');
        }

        _update(balance0, balance1, _reserve0, _reserve1);
        emit Swap(msg.sender, amount0In, amount1In, amount0Out, amount1Out, to);
    }
```
#### Using Uniswap Pair Contract (V2):
- Users must transfer ERC20 tokens to the pair contract and immediately call swap or addLiquidity functions, requiring atomicity.
- Direct EOA interactions are vulnerable to front-running by MEV players.

#### The Role of Periphery Contract:
- **Simplified Approvals**: Users approve their assets to this contract only once.
- **Process**:
  - When adding liquidity or swapping, the router contract is used.
  - It transfers funds to the pair contract and then calls the swap or addLiquidity.
  - These sequential actions in a single transaction ensure atomicity and security.
- **Analogous to Database Transactions**:
  - The operation is similar to writing transactions in a database.
  - If conditions worsen or fail, the entire transaction is rolled back, preventing token loss.
- **Benefits**:
  - Protects from token loss in failed transactions.
  - Manages slippage and other conditional checks.
  - Offers efficient routing across pools, minimizing unnecessary approvals and transactions.

### Conclusion

The introduction of the periphery (or router) contract in Uniswap V2 and V3 effectively resolves the outlined issues. It streamlines the user experience, enhances transaction security, and provides efficient asset routing across different liquidity pools.
