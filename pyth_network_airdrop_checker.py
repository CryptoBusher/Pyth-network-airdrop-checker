import requests
from time import sleep


def check_airdrop(_wallet: str, proxy: str = None):
    url = f'https://airdrop.pyth.network/api/grant/v1/evm_breakdown?identity={_wallet}'

    if proxy:
        _proxies = {
            "http": proxy,
            "https": proxy
        }
        response = requests.get(url, proxies=_proxies)
    else:
        response = requests.get(url)

    print(response.text)


if __name__ == "__main__":
    with open("wallets.txt", "r") as file:
        wallets = [w.strip() for w in file]

    with open("proxies.txt", "r") as file:
        proxies = [p.strip() for p in file]

    for i, wallet in enumerate(wallets):
        try:
            check_airdrop(wallet, proxies[i])
        except IndexError:
            check_airdrop(wallet)
        except Exception as e:
            print(f'Failed to check wallet {wallet}, reason: {e}')
        finally:
            sleep(1)
