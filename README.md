<h1 align="center">
  <br>
  Python Regular Expression Parser
  <br>
</h1>

<h4 align="center">Utility to convert Python Regular Expression to formal definition</h4>

---

## What?

With this code you can convert regular expression given in the Python format to a (close) equivalent formal definition.

For a quick guide on Python regex, see the [official documentation](https://docs.python.org/3/howto/regex.html).

### TODO
- [ ] Add formal definition


## Usage

Run the script with

```bash
python main.py <destination> -e <expression> 
```
where `destination` should be one of `REGEX`, `SYA`, `NFA` or `DFA`.

Other optional arguments include `-s` for strict mode. Here, an error is thrown instead of making any assumptions when converting an expression.
Also, `-d` enables debug mode, which prints conversion steps.





For a complete explanation of command-line arguments see
```bash
python main.py -h
```

## License

MIT License

Copyright (c) 2022 Tobias Kalmbach

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

> [kalmbach.dev](https://www.kalmbach.dev) &nbsp;&middot;&nbsp;
> GitHub [@Tobi2K](https://github.com/Tobi2K) &nbsp;&middot;&nbsp;
> Email [tobias@kalmbach.dev](mailto:tobias@kalmbach.dev)