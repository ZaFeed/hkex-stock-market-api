# HKEX Symbol Lookup: Turn 700 into HKEX:00700

ZaFeed's Hong Kong catalog identifies Tencent as `HKEX:00700`. The leading zeros are part of the **ZaFeed identifier**. Keep the normalized value as text through spreadsheet imports, database writes and API requests.

港股接入示例：把自选股里的 `700`、`00700` 或 `HKEX:00700` 归一成 ZaFeed 的港股标的代码，再查是否出现在公开样本中。

## Import a mixed watchlist

```bash
python3 hkex-symbols.py 700 00005 HKEX:09988
```

Expected identifiers: `HKEX:00700`, `HKEX:00005`, `HKEX:09988`. Each output row includes `inSampleCatalog`. The sample file is a metadata lookup, so a valid code missing from it has no confirmed status. Already-qualified codes from a different exchange, decimals and six-digit inputs fail rather than being silently rewritten.

| Source | Keep as text in ZaFeed |
| --- | --- |
| Tencent: `700` | `HKEX:00700` |
| HSBC: `5` | `HKEX:00005` |
| Xiaomi: `1810` | `HKEX:01810` |
| Alibaba: `9988` | `HKEX:09988` |

## Use the same identifier for the quote

With an active Hong Kong market Key and assigned HTTPS origin:

```bash
ZAFEED_SYMBOL=HKEX:00700 bash market-data.sh quotes
```

The request uses `market=HK`. Market Keys and quote access are described in the [quote API docs](https://www.zafeed.com/docs-quote.html). For additional languages, see the [shared quickstart](https://github.com/ZaFeed/stock-market-data-api).

**Why preserve the prefix and zeros?** Normalization is specific to the receiving service. Use the exact identifier from the [ZaFeed HK directory](https://www.zafeed.com/symbols.html?market=hk) for ZaFeed calls. For exchange trading rules and security information, use [HKEX's securities market documentation](https://www.hkex.com.hk/Global/Exchange/FAQ/Securities-Market/Trading?sc_lang=en).
