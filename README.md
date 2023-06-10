
# What is this?

**Prometheus** is a spelling checker and also a corrector. It uses *pynput* for keyboard hooks and functions. It is worth mentioning that this project is really basic level. If your WPM is above 90, I do not recommend using prometheus since it runs synchronously without word location tracking which might cause complex mistakes if you are typing so fast. It uses `Word` from *textblob* library for confidence check. Feel free to upgrade this. PR's are welcome.



## Features

- Confidence based correction system
- Keyboard hooks for auto-corection
- Basic check to see if it is really a mistake
- Processing in background capability
- Tested on Windows

  
## Install The Requirements

```bash
  pip install requirements.txt -r
```



  
## Licence

This project is licensed under [Apache-2.0](https://choosealicense.com/licenses/apache-2.0/)!

  
