"""
Shared configuration for all benchmark runners.
Reads API keys / tokens from environment variables.
Copy .env.example to .env and fill in your own values.
"""

import os

# DeepSeek API
DS_KEY = os.environ.get("BENCH_DS_KEY", "")

# CST Cloud (中科院磐石)
CST_KEY = os.environ.get("BENCH_CST_KEY", "")

# Kimi K2.6 (Moonshot)
KIMI_TOKEN = os.environ.get("BENCH_KIMI_TOKEN", "")

# MiMo V2.5 (Xiaomi)
MIMO_TOKEN = os.environ.get("BENCH_MIMO_TOKEN", "")

# Optional: Anthropic OAuth Max (for opus)
# When unset, claude.exe falls back to OAuth Max subscription.
ANTHROPIC_BASE_URL = os.environ.get("ANTHROPIC_BASE_URL", "")
ANTHROPIC_AUTH_TOKEN = os.environ.get("ANTHROPIC_AUTH_TOKEN", "")


def get_kimi_env():
    return {
        "ANTHROPIC_BASE_URL": "https://api.moonshot.cn/anthropic",
        "ANTHROPIC_AUTH_TOKEN": KIMI_TOKEN,
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "kimi-k2.6",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "kimi-k2.6",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "kimi-k2.6",
        "CLAUDE_CODE_SUBAGENT_MODEL": "kimi-k2.6",
        "CLAUDE_CODE_EFFORT_LEVEL": "max",
        "ENABLE_TOOL_SEARCH": "false",
    }


def get_ds_cc_env():
    return {
        "ANTHROPIC_BASE_URL": "https://api.deepseek.com/anthropic",
        "ANTHROPIC_AUTH_TOKEN": DS_KEY,
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "deepseek-v4-pro[1m]",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "deepseek-v4-pro[1m]",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "deepseek-v4-flash",
        "CLAUDE_CODE_SUBAGENT_MODEL": "deepseek-v4-flash",
        "CLAUDE_CODE_EFFORT_LEVEL": "max",
    }


def get_mimo_env():
    return {
        "ANTHROPIC_BASE_URL": "https://token-plan-cn.xiaomimimo.com/anthropic",
        "ANTHROPIC_AUTH_TOKEN": MIMO_TOKEN,
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "mimo-v2.5-pro",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "mimo-v2.5-pro",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "mimo-v2.5",
        "CLAUDE_CODE_SUBAGENT_MODEL": "mimo-v2.5",
        "CLAUDE_CODE_EFFORT_LEVEL": "max",
    }


def get_panshi_env():
    return {
        "ANTHROPIC_BASE_URL": "https://uni-api.cstcloud.cn",
        "ANTHROPIC_AUTH_TOKEN": CST_KEY,
        "ANTHROPIC_DEFAULT_OPUS_MODEL": "S1-Base-Ultra",
        "ANTHROPIC_DEFAULT_SONNET_MODEL": "S1-Base-Ultra",
        "ANTHROPIC_DEFAULT_HAIKU_MODEL": "S1-Base-Pro",
        "CLAUDE_CODE_SUBAGENT_MODEL": "S1-Base-Pro",
        "CLAUDE_CODE_EFFORT_LEVEL": "max",
    }
