# pylint: disable=all
# flake8: noqa
from typing import Any
from typing import List
from typing import Optional

from beancount.core.data import Directive
from beancount.core.data import Entries

def get_accounts_use_map(entries: Entries): ...
def get_accounts(entries: Entries): ...
def get_entry_accounts(entry: Directive): ...
def get_account_components(entries: Entries): ...
def get_all_tags(entries: Entries) -> List[str]: ...
def get_all_payees(entries: Entries): ...
def get_all_links(entries: Entries) -> List[str]: ...
def get_leveln_parent_accounts(
    account_names: Any, level: Any, nrepeats: int = ...
): ...
def get_dict_accounts(account_names: Any): ...
def get_min_max_dates(entries: Entries, types: Optional[Any] = ...): ...
def get_active_years(entries: Entries) -> List[int]: ...
def get_account_open_close(entries: Entries): ...
def get_commodity_map(entries: Entries, create_missing: bool = ...): ...
def get_values_meta(
    name_to_entries_map: Any, *meta_keys: Any, default: Optional[Any] = ...
): ...
