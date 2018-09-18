from __future__ import print_function
from __future__ import absolute_import

import argparse

from argstat import Argstat

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    input_args = parser.add_argument_group('Input args')
    input_args.add_argument('--train_target', type=str,
                            default='C', choices=['C', 'C+E'])
    input_args.add_argument('--test_target', type=str,
                            default='C', choices=['C', 'C+E'])
    input_args.add_argument('--rec_size', type=int, default=20)
    input_args.add_argument('--input_size', type=int, default=18)
    input_args.add_argument('--num_vital', type=int, default=6)
    input_args.add_argument('--cut_window', type=int, default=-1)
    input_args.add_argument('--skip_prob', type=float, default=-1)
    input_args.add_argument('--skip_mask', type=int, default=-1)
    input_args.add_argument('--target_vital', type=int, default=0)

    train_args = parser.add_argument_group('Train args')
    train_args.add_argument('--num_epochs', type=int, default=10)
    train_args.add_argument('--batch_size', type=int, default=120)
    train_args.add_argument('--lr', type=float, default=0.001)

    base_args = parser.add_argument_group('Base args')
    base_args.add_argument('--save_path', type=str, default='test')
    base_args.add_argument('--weight_path', type=str)
    base_args.add_argument('--gpu', type=str, default='-1')
    base_args.add_argument('--device', type=str)
    base_args.add_argument('--mode', type=str, default='base',
                           choices=['base', 'single'])

    argstat = Argstat(parser)
    print (argstat)
