# Run-length Encoder

Read about it [here](https://en.wikipedia.org/wiki/Run-length_encoding)

This does not encode runs less than 3

- `AA` will not change to `2A`
- `A` will not change to `1A`

Example
------
`WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW`
will become
`12WB12W3B24WB14W`
