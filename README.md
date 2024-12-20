# mydatanaut - ΑΑΔΕ/myData Python library
`mydatanaut` library provides a convenient way for accessing myData REST API from applications written in the Python language. 

### Introduction & Disclaimer
This library was authored primarily to aid the relay of invoices generated by Stripe to AADE/myData in a production django application. Although the current code is being used in production it **should not be considered mature, safe and feature-proof** for your production environment.

You should treat this library as a basis for contributing improvements such as implementation of new features, bug fixes, test cases and refactorings vs having to implement the API from scratch on your own. This library will be maintained/improved only to the extend the original author sees fit to serve the purposes of other software.

⭐️ Contributions are welcome!

### Installation
```
pip install --upgrade mydatanaut
```

### Usage
Please see [examples](https://github.com/attheodo/mydatanaut/tree/main/example)

### Documentation
- Official myDATA webpage: [AADE myDATA](https://www.aade.gr/mydata)
- Official myDATA documentation: [AADE myDATA REST API v1.0.9](https://www.aade.gr/sites/default/files/2024-07/myDATA%20API%20Documentation%20v1.0.9_official_erp.pdf)

In order to use this package, you will need a `user id` and a `subscription key`. You can get these credentials by signing up to mydata rest api.

- Development/Sandbox: [MyData Development API](https://mydata-dev-register.azurewebsites.net/)
- Production: [MyData](https://www.aade.gr/mydata)


### Credits
Progress in developing this library would have been extremely slow and frustrating if not for the PHP package [aade-mydata](https://github.com/firebed/aade-mydata) put together by [Okan Giritli](https://github.com/firebed). 

### License
This library is licenses under the [MIT License](License.md)
Copyright 2024 © Thanos "attheodo" Theodoridis
