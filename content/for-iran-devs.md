
# راهکار برای توسعه‌دهندگان در ایران برای مقابله با فیلترینگ و تحریم

## محدودیت‌ها
1. سرعت اینترنت
2. فیلتر شدن
3. تحریم بودن (۴۰۳ خوردن و نگرانی برای لاگ شدن IP ایران روی سرورهای شرکت‌ها و AWS و ...)

## نیازمندی‌ها
الف. یک سرور خارج ایران با ریسورس‌های متناسب با نیازتون (منظور رم و CPU و حافظه هستش)
   - بسته به stack و نرم‌افزارهایی که استفاده می‌کنید می‌تونه متفاوت باشه. مثلا اگه کامپایل زیاد می‌کنید CPU خوب باشه تایم کمتری صبر می‌کنید یا اگه داکر نیاز دارید اون رو هم در نظر بگیرید و ...

ب. یه کانکشن اینترنت که بتونید به اون سرور وصل بشید با SSH
   - بعضی موقع‌ها سرور رو اگه فقط خودتون وصل بشید نمیزنن ولی اگه زدن هم یه فیلتر شکن داشته باشین که بهتون یه کانکشن نسبتا stable و نه الزاما سریع بده کارها رو در میاره

پ. تجربه کار با لینوکس

## فرایند

### 1. تهیه سرور متناسب با نیاز هاتون
- از سایت‌هایی مثل Bithost می‌تونید با کریپتو هم سرور بگیرید و سایت‌های زیادی وجود داره برای گرفتن سرور با کریپتو.

### 2. نصب tmux یا نرم‌افزار مشابه رو سرور
- [tmux VS screen](https://www.reddit.com/r/archlinux/comments/d41c1w/screen_vs_tmux/)
  - که بتونید به session‌های قبلیتون وصل بشید یا اگه کانکشنتون قطع شدش مشکلی تو فرایند اجرا شدن یه کامند یا ... به وجود نیاد و بتونید بعد از وصل شدن به ادامه کار بپردازید.

### 3. نصب ابزارهای کمکی
- اگه از چیزهای دیگه‌ای جای bash استفاده می‌کنید، اون‌ها رو هم نصب کنید. این‌ها چیزهایی که زندگیم رو راحت‌تر کرده:
  - [Oh My Zsh](https://ohmyz.sh/)
  - [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)

### 4. کانفیگ سرور
- به طور کلی انگار یه سیستم لینوکسی جدید خریدید و هر کانفیگی معمولا روی سیستم جدید انجام میدید رو این سرور هم انجام بدین. انگار ترمینال اون، ترمینال سیستم لوکال خودتونه (make the server like your home).

### 5. کانفیگ SSH Key
- کانفیگ کردن SSH-Key‌ها مرتبط با اکانت گیتهاب/گیت لب اتون

### 6. نصب ابزارهای مرتبط با استک
- نصب ابزارهای مرتبط با استک: npm, yarn, cargo, foundry, go, ...

### 7. ساختن ssh-config
- ساختن ssh-config روی سیستم خودتون برای وصل شدن به سرور
  - [لینک](https://betterprogramming.pub/a-step-by-step-walkthrough-to-create-your-first-ssh-config-file-f01267b4eacb) 
  - (از ChatGPT بپرسید هم سریع‌تر به نتیجه می‌رسید)

### 8. اتصال به VS Code
- باز کردن VS Code و باز کردن command palette (روی مک Command + Shift + P)
  - نوشتن connect to host و روی گزینه‌ای که آورد کلیک کنید و ssh-config اتون رو لود کنید و بعد با کلیک کردن روی کانفیگ مورد نظر، VS Code شما به سرور مورد نظرتون وصل شده و هم دسترسی ترمینال دارین اونجا هم می‌تونید کد بنویسید و فایل‌ها رو هم از بار سمت چپ می‌تونید کنترل کنید.

### 9. کلون کردن ریپوها
- می‌تونید repo‌هاتون رو clone کنید و فایل‌هاتون رو بچینید و با دستور `code path/repo-name` هم می‌تونید VS Code رو توی اون دایرکتوری مورد نظرتون باز کنید و ...

### 10. نصب اکستنشن‌های VS Code
- اکستنشن‌های VS Code ای که استفاده می‌کنید رو هم نصب کنید (مثل rust analyzer, solidity visual developer, git lens ...)

### 11. مدیریت داکر با Portainer
- اگه با داکر هم زیاد کار دارید و حوصله ندارید زیاد کامند‌های داکر بنویسید و یه محیط شبیه Docker Desktop دوست دارید داشته باشید برای مدیریت و ...
  - می‌تونید Portainer رو نصب کنید و با Nginx روی IP سرور اش کنید و با browser اتون بهش وصل بشید.
    - (البته قبلش خود داکر, داکر کامپوز رو نیاز دارین رو سرور نصب کنید)
    - [Portainer](https://www.portainer.io/)
    - [Docs](https://docs.portainer.io/start/install-ce)

### 12. استفاده از SSH-Tunneling
- اگه دوست داشتین به دیتابیس‌هاتون وصل بشین معمولا Data Base Viewer‌ها مثل pgAdmin از SSH-Tunneling ساپورت می‌کنن می‌تونید استفاده کنید.

### 13. مدیریت پورت‌ها با Nginx
- اگه هم کار فرانت دارید یا نیاز دارید یه چیزی رو روی یه پورتی بیارید بالا و تستش کنید
  - توی Nginx سرور اتون یه Basic Auth ست کنید برای یه پورت یا چند تا و وقتی نیاز داشتید چیزی رو تست کنید مثل لوکالتون ران کنید و port proxy از لوکال به IP پابلیک رو توی Nginx هندل کنید (ترجیحا این پورت‌ها رو پرت بزارید که indexer های سطح اینترنت اذیت نکنن سرور رو).

بعد از همه این مراحل موقع کار VS Code رو باز می‌کنید و وصل می‌شید به سرور بعد اش اگه دوست داشتین سشن‌های tmux ای که باز داشتین و ادامه کار.

خلاصه که بعد از این مراحل الان یه محیط توسعه دارید که دغدغه سرعت اینترنت برای نصب پکیج‌ها و ... و مشکل تحریم (۴۰۳) و فیلتر بودن رو نداره.

طبیعه که این کار احتمالا برای یک سری توسعه‌دهنده‌ها مثل توسعه‌دهنده‌های موبایل و ... ممکنه شدنی نباشه ولی برای بچه‌های بلاکچینی و بک اندی کاملا جواب می‌تونه بده نیازهاشون رو.

این ویدئو هم کوتاه و خوب بودش برای نشون دادن وصل شدن و ...

- [ویدئو](https://www.youtube.com/watch?v=miyD4c1dnTU)

اگه هم که کاربر vim, neovim هستید پوزش بابت زیاده‌گویی‌ها 😂🍻
