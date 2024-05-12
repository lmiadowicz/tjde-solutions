from urllib.parse import urlparse, parse_qs

from src.logger import logger


def parse_urls(df):
    logger.info("Starting URL parsing")

    if df.empty:
        raise ValueError("Empty DataFrame provided.")

    df['parsed'] = df['url'].apply(lambda url: urlparse(url).query)

    # Extract marketing params from query string
    for param in ["a_bucket", "a_type", "a_source", "a_v",
                  "a_g_campaignid", "a_g_keyword", "a_g_adgroupid", "a_g_creative"]:
        df[param] = df['parsed'].apply(lambda x: parse_qs(x).get(param, [""])[0])

    df = df.rename(columns={
        "a_bucket": "ad_bucket",
        "a_type": "ad_type",
        "a_source": "ad_source",
        "a_v": "schema_version",
        "a_g_campaignid": "ad_campaign_id",
        "a_g_keyword": "ad_keyword",
        "a_g_adgroupid": "ad_group_id",
        "a_g_creative": "ad_creative",
    })

    logger.info("URL parsing completed successfully.")

    return df[[
        "url", "ad_bucket", "ad_type", "ad_source", "schema_version",
        "ad_campaign_id", "ad_keyword", "ad_group_id", "ad_creative"
    ]]
