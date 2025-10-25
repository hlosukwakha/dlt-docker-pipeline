import os
import time
import requests
import dlt

#python3 -m pip install "dlt[postgres]"

HN_BASE = "https://hacker-news.firebaseio.com/v0"

def get_top_story_ids(limit=100):
    resp = requests.get(f"{HN_BASE}/topstories.json", timeout=30)
    resp.raise_for_status()
    return resp.json()[:limit]

def get_item(item_id):
    r = requests.get(f"{HN_BASE}/item/{item_id}.json", timeout=30)
    r.raise_for_status()
    return r.json()

def iter_top_stories(limit=100):
    for sid in get_top_story_ids(limit=limit):
        try:
            item = get_item(sid)
            if item is None:
                continue
            yield item
        except requests.HTTPError as e:
            print(f"warn: failed to fetch item {sid}: {e}")
            continue

def postgres_credentials_from_env():
    return {
        "database": os.getenv("POSTGRES_DB", "dlt"),
        "host": os.getenv("POSTGRES_HOST", "postgres"),
        "port": int(os.getenv("POSTGRES_PORT", "5432")),
        "username": os.getenv("POSTGRES_USER", "dlt"),
        "password": os.getenv("POSTGRES_PASSWORD", "dlt"),
    }

def main():
    destination_name = os.getenv("DLT_DESTINATION") or "postgres"

    # Configure destination creds via dlt.secrets (no destination_credentials in run)
    if destination_name == "postgres":
        dlt.secrets["destination.postgres.credentials"] = postgres_credentials_from_env()

    pipeline = dlt.pipeline(
        pipeline_name="hn_to_postgres",
        destination=destination_name,
        dataset_name="hn_raw",
    )

    print("Starting extract of Hacker News top stories...")
    # Wrap the generator as a dlt.resource with a primary key for proper MERGE
    stories = dlt.resource(
        iter_top_stories(limit=150),
        name="stories",
        primary_key="id"
    )

    load_info = pipeline.run(
        stories,
        write_disposition="merge"
    )

    print(load_info)
    print("Done.")

if __name__ == "__main__":
    main()