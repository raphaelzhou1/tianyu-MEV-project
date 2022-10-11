## tianyu-defi-parameters-gathering is a project to build MEV bots and gain expertise on certain types of MEV attack vectors.

This README.md is formatted according to https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

## Introduction on MEV Strategies:
2 general financial categories:
Pure Revenue (exploit-based) vs. risky strategies

Risky: Auction-based, collusion-based (“On the instability of bitcoin without the block reward”, “Smart Contracts for Bribing Miners”)

2 general methodological categories of search strategies:
Numerical search vs. symbolic-execution search

# References:
“Flash boys 2.0: frontrunning in decentralized exchanges, miner extractable value, and consensus instability” + “SoK: Transparent Dishonesty: frontrunning attacks on Blockchain” + “Sok: Algorithmic incentive manipulation attacks on permissionless pow cryptocurrencies”

# Notable MEV mitigation regimes:
Robert Miller was taking about symbolic-execution search risky strategies that Flash Bots is working
Flash Boys 2.0 paper compared Pure Revenue (exploit-based) vs. risky strategies, proposed PGA (auction-based) as most promising of the risky strategies

## Strategies:
# MetaSecure Plan Proposal:
Based on such categorization, MetaSecure's best expertise is to do pure-revenue symbolic-execution search + collusion-based search

My DeFi background most justifies a risky strategies auction-based search

# Atomic-transaction MEV arbitrage:

# Liquidation Bots:
Aave
Aave Liquidation doc: https://docs.aave.com/developers/guides/liquidations
Aave Health Factor Monitoring
Kirsche’s Aave liquidation bot: https://github.com/dkirsche/aave-liquidator

# Pure Revenue Strategies

# Gas Auction Strategies
[2208.02036] Computing Bayes Nash Equilibrium Strategies in Auction Games via Simultaneous Online Dual Averaging


# Symbolic Execution Strategies
https://www.youtube.com/watch?v=VkSR9jz_C-0


Timeline/Goals: 
October
Tianyu: Finish CryptoZombie tutorial
Gather on-chain data to analyze existing transaction parameters (/delta, /Delta; /G)
Build an initial liquidation bot by End of Month 
Tianyu: replicate Kirsche’s Aave Liquidation Bot



November
Build an initial long-tail MEV bot
Joanne: Read https://github.com/bzhang42/symbolic-searcher/blob/main/research_report.pdf




December
