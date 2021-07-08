# Docker Test Environments Tutorial

## Pulling
First we need to download our docker image.

```bash
docker pull ghcr.io/decentra-network/api:latest
```
<walkthrough-footnote>Decentra Network</walkthrough-footnote>

## Name Changing
Second we will make its name available for use.

```bash
docker image tag ghcr.io/decentra-network/api decentra-network-api
```
<walkthrough-footnote>Decentra Network</walkthrough-footnote>

## Running The Auto Tests
Finaly we run our automated test tool, it sets up and tests the network for us.

```bash
python3 test_environments/docker/test_decentra_network_docker.py
```
<walkthrough-footnote>Decentra Network</walkthrough-footnote>
## Conclusion
<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>



<walkthrough-footnote>Decentra Network</walkthrough-footnote>