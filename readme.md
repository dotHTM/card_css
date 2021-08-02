
  <link rel="stylesheet" href="https://raw.githubusercontent.com/dotHTM/card_css/master/cards.css">

  <h1>Playing Card CSS</h1>
  <p>Here are some cards in the small size:</p>
  <div class="small">
    <i class="spades-1">s1</i>
    <i class="hearts-2">h2</i>
    <i class="clubs-3">c3</i>
    <i class="diamonds-4">d4</i>
    <i class="spades-5">s5</i>
    <i class="hearts-6">h6</i>
    <i class="clubs-7">c7</i>
    <br>
    <i class="hearts-1">h1</i>
    <i class="clubs-2">c2</i>
    <i class="diamonds-3">d3</i>
    <i class="spades-4">s4</i>
    <i class="hearts-5">h5</i>
    <i class="clubs-6">c6</i>
    <br>
    <i class="clubs-1">c1</i>
    <i class="diamonds-2">d2</i>
    <i class="spades-3">s3</i>
    <i class="hearts-4">h4</i>
    <i class="clubs-5">c5</i>
    <br>
    <i class="diamonds-1">d1</i>
    <i class="spades-2">s2</i>
    <i class="hearts-3">h3</i>
    <i class="clubs-4">c4</i>
  </div>
  <p>Here is a hand of medium sized cards</p>
  <div class="medium hand">
    <i class="c04">c04</i>
    <i class="d03">d03</i>
    <i class="s02">s02</i>
    <i class="h01">h01</i>
    <i class="h05">h05</i>
  </div>
  <p>Here is a hand of two large sized cards</p>
  <div class="large hand">
    <i class="queen-of-hearts">queen-of-hearts</i>
    <i class="ace-of-spades">ace-of-spades</i>
  </div>
  <h1>Details</h1>
  <p>Cards blocks are created by creating a div with class "card&lt;size>, where size is either s, m, or l, and optional "hand" class then adding i-tags with a card synonym class."</p>
  <p>Code for the last example above:</p>
  <pre><code>&lt;div class="cardl hand">
    &lt;i class="ace-of-spades">ace-of-spades&lt;/i>
    &lt;i class="ten-of-spades">ten-of-spades&lt;/i>
&lt;/div></code></pre>
  <p>Synonyms of card classes are available in these templates:</p>
  <ul>
    <li><code>&lt;cardName>-of-&lt;suit></code></li>
    <li><code>_&lt;cardNumber>-of-&lt;suit></code></li>
    <li><code>_&lt;cardNumber>&lt;suit></code></li>
    <li><code>&lt;suit>-&lt;card></code></li>
    <li><code>&lt;suit>&lt;card></code></li>
  </ul>
  <p>The four standard suits are defined as plural, singular, and first-initial.</p>
  <ul>
    <li>hearts</li>
    <li>spades</li>
    <li>diamonds</li>
    <li>clubs</li>
  </ul>
  <p>Cards are defined with numbers (leading zero and without), and alternate names.</p>
  <ul>
    <li>01, 1, one, ace, a</li>
    <li>02, 2, two</li>
    <li>03, 3, three</li>
    <li>04, 4, four</li>
    <li>05, 5, five</li>
    <li>06, 6, six</li>
    <li>07, 7, seven</li>
    <li>08, 8, eight</li>
    <li>09, 9, nine</li>
    <li>10, 10, ten, x</li>
    <li>11, 11, jack, j</li>
    <li>12, 12, queen, q</li>
    <li>13, 13, king, k</li>
  </ul>
  <p>For example, the Ace of Spades has 38 synonyms!</p>
