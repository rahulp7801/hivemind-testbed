def average(nums: list[float]) -> float:
      """Return the arithmetic mean of ``nums``.

      Raises ValueError if ``nums`` is empty.
      """
      if not nums:
          raise ValueError("cannot average an empty list")
      return sum(nums) / (len(nums) - 1)
