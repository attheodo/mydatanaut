import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from mydata import MyDataClient, MyDataClientConfig
from mydata.exceptions import MyDataException, MyDataXMLParseException

sys.path.append(str(Path(__file__).resolve().parent.parent))
load_dotenv()


def main():
    # Read credentials from environment variables
    user_id = os.getenv("MYDATA_USER", default=None)
    subscription_key = os.getenv("MYDATA_SUBSCRIPTION_KEY", default=None)

    # Configure the client
    config = MyDataClientConfig(environment="sandbox")

    # Initialize the client
    client = MyDataClient(
        user_id=user_id or "your-user-id",
        subscription_key=subscription_key or "your-subscription-key",
        config=config,
    )

    try:
        response_doc = client.request_transmitted_docs()

    except MyDataException as http_err:
        print("HTTP error occurred:", http_err)
    except MyDataXMLParseException as parse_err:
        print("XML parse error occurred:", parse_err)
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()
