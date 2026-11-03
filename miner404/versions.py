"""The plan this submission runs."""

from __future__ import annotations

from .pipeline import Draft, StagePlan, Step

ACTIVE_PLAN = StagePlan(drafts=(Draft(start='plain', model='gpt-6.1-sol', effort='high'), Draft(start='proportions', model='gpt-6.1-sol', effort='high'), Draft(start='plain', model='gpt-6.1-sol', effort='high'), Draft(start='proportions', model='gpt-6.1-sol', effort='high'), Draft(start='plain', model='gpt-6.1-sol', effort='high'), Draft(start='proportions', model='gpt-6.1-sol', effort='high')), steps=(Step(rewrites=(('gpt-6.1-sol', 'high'),), lineage=(), keep=2, focus=()), Step(rewrites=(('gpt-6-astra', 'high'),), lineage=(), keep=1, focus=()), Step(rewrites=(('gpt-6.1-sol', 'high'), ('gpt-6.1-sol', 'xhigh')), lineage=(), keep=1, focus=()), Step(rewrites=(('gpt-6.1-sol', 'xhigh'),), lineage=(), keep=1, focus=()), Step(rewrites=(('gpt-6.1-sol', 'xhigh'),), lineage=(), keep=1, focus=())), draft_keep=3, pose=True, fill=0.99, glow=0.0, measured=False, outline_fit=True)
