# argstat
Beautiful printer for arguments (argparse) inspired by youngnam

## Install
```
$ pip install argstat
```

## Example 1
```
>>> from argstat import Argstat # ①
>>> import argparse
>>>
>>> parser = argparse.ArgumentParser()
>>> input_args = parser.add_argument_group('Input args')
>>> input_args.add_argument('--train_target', type=str,
>>>                         default='C', choices=['C', 'C+E'])
>>> input_args.add_argument('--test_target', type=str,
>>>                         default='C', choices=['C', 'C+E'])
>>> input_args.add_argument('--rec_size', type=int, default=111)
>>> input_args.add_argument('--input_size', type=int, default=222)
>>> input_args.add_argument('--num_vital', type=int, default=333)
>>> input_args.add_argument('--cut_window', type=int, default=444)
>>> input_args.add_argument('--skip_prob', type=float, default=555)
>>> input_args.add_argument('--skip_mask', type=int, default=666)
>>> input_args.add_argument('--target_vital', type=int, default=777)
>>>
>>> train_args = parser.add_argument_group('Train args')
>>> train_args.add_argument('--num_epochs', type=int, default=888)
>>> train_args.add_argument('--batch_size', type=int, default=999)
>>> train_args.add_argument('--lr', type=float, default=0.1234)
>>>
>>> base_args = parser.add_argument_group('Base args')
>>> base_args.add_argument('--save_path', type=str, default='test long path')
>>> base_args.add_argument('--weight_path', type=str)
>>> base_args.add_argument('--gpu', type=str, default='1234')
>>> base_args.add_argument('--device', type=str)
>>> base_args.add_argument('--mode', type=str, default='base',
>>>                        choices=['base', 'single']) # ②
>>>
>>> argstat = Argstat(parser)
>>> print (argstat)
```

<img width="250" alt="screenshot" src="https://user-images.githubusercontent.com/3329885/45678036-8eb8b100-bb70-11e8-8205-94c7dcd604a1.png">


## Example 2
```
>>> ① ~ ②
>>> argstat = Argstat(parser, False)
>>> print (argstat)
```

## Example 3
```
>>> ① ~ ②
>>> from six.moves import cStringIO as StringIO
>>> argstat = Argstat(parser)
>>> print (argstat.print_to(StringIO(), False).getvalue())
```

## Example 4
```
>>> ① ~ ②
>>> argstat = Argstat(parser)
>>> print (argstat.jsonify())
```

## Example 5
```
>>> ① ~ ②
>>> argstat = Argstat(parser)
>>> with open("path","w") as fp:
>>>     argstat.print_to(fp, False)
```
