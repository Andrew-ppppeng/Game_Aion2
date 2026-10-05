# aion 2 specs — requirements/download refresh

Reviewed 2026-10-04. Existing `/download#pc-requirements` retained. Also carries the collected Taiwan-install intent at `/download#taiwan-client`.

## Direction and sources

- Google suggestions observed by root: specs requirements, requirements, requirements pc/mobile, recommended specs, pc specs, minimum specs, mobile specs. No fabricated phone requirements; ambiguous weight suggestion excluded.
- Official Global Steam appdetails: https://store.steampowered.com/api/appdetails?appids=3393110&cc=us&l=english . Retrieval `steam-appdetails.json`, HTTP 200 on Oct 4, Global/App 3393110. PC configuration unchanged: Win10/11 64-bit; minimum Ryzen 5 2600/i5-10500, 8 GB RAM, GTX1050Ti4GB; recommended Ryzen73700X/i7-11700,16GB,RTX20708GB; DX12/broadband/100GB free/SSD recommended; FHD Very Low vs Low. Steam public page web tool was region blocked; API succeeded. Storage is free space, not download size. Windows=true/mac=false/linux=false describes the listing, not an impossibility of all unofficial device use.
- Official country-specific PURPLE notice: https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd3200a279104f7d9d5eeb ; original publication 2026-09-30, Oct 4 `purple-region.json` current public article. Preserve the five-country launcher region fix; account country is not a launcher setting.
- Windows diagnostic operation: https://support.microsoft.com/en-us/windows/hardware/display-graphics/microsoft-basic-display-adapter-in-windows ; Oct 4 `windows-dxdiag.json`, Windows10/11. Microsoft confirms Run/dxdiag/Display adapter steps. https://support.microsoft.com/en-us/windows/hardware/display-graphics/hdr-settings-in-windows describes System tab; no game performance test is claimed.
- Taiwan official download: https://tw.ncsoft.com/aion2/download/index ; Oct 4 source archive in adjacent `../secondary-updates/tw-download.html`, `-text.txt`, `-request.json`. TW installer steps PurpleInstaller → PURPLE STORE AION2 → lobby 安裝遊戲. TW CPU variants differ from Global; no configuration mixed.
- Official Global Launch FAQ (Oct 1): https://store.steampowered.com/news/app/3393110?emclan=103582791475596239&emgid=680761758839734961 . Fresh Oct 4 Steam ISteamNews archive `../secondary-updates/steam-global-news.json`, title Launch FAQ/gid 1845383656377634. Steam-only play needs no PURPLE link; linking required to access same character/progress across both. Shared Global content/servers. TW/KR progress does not transfer. Current official support is Windows PC Steam/PURPLE; do not infer a phone installer.

## Implemented and limits

- All four languages: specs in metadata/quick answer; retain complete configuration table and 100GB/preset distinctions.
- Added PC self-check via dxdiag, drive-free-space and minimum/recommended starting preset guidance without FPS promises.
- Explicit Global PC scope, separate regional mobile clients, working platform-support link.
- Steam optional linking and separate TW installer steps; retained official installer links and older installation/troubleshooting details.
- TW installation does not answer foreign-account eligibility, verification, payment or VPN legality/operation. No unsupported account, country-bypass or foreign-access recipe added.
