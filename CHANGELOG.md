# Recent Changes

## v2.0.0 - 2024-03-29

### Added
- **Attributes:**
  - `is_empty`: Indicates whether the tree is empty or not.
  - `type`: Type of elements stored in the tree.
  - `height`: Height of the tree.
  - `min_value`: Minimum value stored in the tree.
  - `max_value`: Maximum value stored in the tree.
- **Methods:**
  - `search(*args)`: Searches for elements in the tree and returns True if found.
  - `insert(*args)`: Inserts elements into the tree and returns the current instance.
  - `is_compatible(*args)`: Verifies if elements are compatible with the tree's type.
  - `clear()`: Removes all elements from the tree, leaving it empty.

### Changed
- **Methods:**
  - `remove(value)`: Now accepts multiple values and returns the current tree instance. Renamed from `remove(value)` to `remove(*args)`.
  - `exist(value)`: Renamed to `__exists__(value)`.
  - `stabilize()`: Now returns the current tree instance.

### Removed
- **Methods:**
  - `add(value)`: Replaced by `insert`.
  - `min()`: Replaced by the `min_value` attribute.
  - `max()`: Replaced by the `max_value` attribute.
  - `size()`: Method no longer available.
  - `height()`: Method no longer available.
  - `get(index=0)`: Method no longer available.