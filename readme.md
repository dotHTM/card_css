# Details

Cards blocks are created by creating a div with class "card<size>, where size is either "small", "medium", or "large", and optional "hand" class then adding i-tags with a card synonym class."

Example:

```html
<div class="large hand">
  <i class="ace-of-spades">ace-of-spades</i>
  <i class="ten-of-spades">ten-of-spades</i>
</div>
```

Synonyms of card classes are available in these templates:

- `<cardName>-of-<suit>`
- `_<cardNumber>-of-<suit>`
- `_<cardNumber><suit>`
- `<suit>-<card>`
- `<suit><card>`

The four standard suits are defined as plural, singular, and first-initial.

- `hearts`
- `spades`
- `diamonds`
- `clubs`

Cards are defined with numbers (leading zero or without), and alternate names.

- `01`, `1`, `one`, `ace`, `a`
- `02`, `2`, `two`
- `03`, `3`, `three`
- `04`, `4`, `four`
- `05`, `5`, `five`
- `06`, `6`, `six`
- `07`, `7`, `seven`
- `08`, `8`, `eight`
- `09`, `9`, `nine`
- `10`, `10`, `ten`, `x`
- `11`, `11`, `jack`, `j`
- `12`, `12`, `queen`, `q`
- `13`, `13`, `king`, `k`

For example, the Ace of Spades has 38 synonyms!
