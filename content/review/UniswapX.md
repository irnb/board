# UniswapX Analysis and Suggestions

## :mag_right: Overview
I've reviewed the [UniswapX Whitepaper](https://uniswap.org/whitepaper-uniswapx.pdf) and various diagrams related to its architecture:

![Diagram 1](https://github.com/irnb/board/assets/41897852/3b9ed8ba-7813-4ef4-82f6-8a4ef2defd34)
<img width="2231" alt="UniswapX Architecture" src="https://github.com/irnb/board/assets/41897852/39f45fbf-be99-4627-a4ea-6d79f3a01237">
![UniswapX System Overview](https://github.com/irnb/board/assets/41897852/b5611834-5bdd-4cd4-9eb8-afeee2c5a172)

## :memo: Notes

### Permits2 
:star2: The Permits2 concept appears to be a highly innovative approach. It allows a user to give one-time approval for a token, after which this contract facilitates the use of this approval in other contracts through signed messages. This concept has potential applications in various DeFi protocols.

### Bridge Architecture
:bridge_at_night: Further research on bridge architecture is needed to fully understand its implications and applications within UniswapX.

### MEV
:shield: UniswapX's approach with fillers doesn't completely solve the MEV problem. Instead, it introduces competition between fillers (including MEV searchers and market makers). The outcome of this competition helps users to be less affected by MEV attackers.


## :loudspeaker: Outputs

1. **Axiom Community Outreach**
   
   :speech_balloon: Message to Axiom Community highlighting that Axiom could be a beneficial feature for UniswapX, especially for fraudProof crosschain messaging.

   ![Axiom Context](https://github.com/irnb/board/assets/41897852/bddfda3d-ef05-47af-b1a5-536682f60a73)

3. **GitHub Issue Creation**
   
   :bulb: Suggestion to UniswapX: Implement "Filler Specific Bond Pools" to reduce operational costs for fillers. This approach involves managing assets within the contract, decreasing the need for frequent token transfers.
   - [GitHub Issue Link](https://github.com/Uniswap/UniswapX/issues/216)
