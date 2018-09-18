from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import argparse
from blessings import Terminal
import sys


class Argstat:
    def __init__(self, parser, with_colors=True, argv=sys.argv[1:]):
        self.args = parser.parse_args()
        self.with_colors = with_colors
        self.arg_groups = {}
        self.max_argname_length = 0
        self.max_value_length = 0

        # https://stackoverflow.com/questions/31519997/is-it-possible-to-only-parse-one-argument-groups-parameters-with-argparse
        for group in parser._action_groups:
            group_dict = {}
            self.max_argname_length = max(self.max_argname_length,
                                          len(group.title))
            for a in group._group_actions:
                self.max_argname_length = max(self.max_argname_length,
                                              len(a.dest))
                value = getattr(self.args, a.dest, None)
                self.max_value_length = max(self.max_value_length,
                                            len(str(value)))
                group_dict[a.dest] = value
            group_dict = {a.dest: getattr(self.args, a.dest, None)
                          for a in group._group_actions}
            self.arg_groups[group.title] = argparse.Namespace(**group_dict)

    def __repr__(self):
        return self.print_to(StringIO(), self.with_colors).getvalue()

    def print_to(self, fp, with_colors=None, term=Terminal()):
        reps = ""
        colors = {}
        if with_colors is not None and with_colors:
            colors['normal'] = term.normal
            colors['group'] = term.blue
            colors['noargname'] = term.red
            colors['argname'] = term.cyan
            colors['value'] = term.green
            colors['line'] = term.color(9)
        else:
            colors['normal'] = colors['group'] = colors['noargname']\
                    = colors['argname'] = colors['value'] = colors['line']\
                    = term.normal

        NO_ARGUMENT = "No Arguments"

        total_line_length = self.max_argname_length+self.max_value_length+4
        for group_title in self.arg_groups:
            s = "{line}o- {group}{} {line}{}o\n"
            reps += s.format(group_title,
                             "-"*(total_line_length-len(group_title)-3),
                             **colors)
            args = self.arg_groups[group_title]
            if args == argparse.Namespace():
                s = "{line}|{noargname}{:>"+str(self.max_argname_length)+"}"
                s += "   {value}{:<"+str(self.max_value_length)+"} {line}|\n"
                reps += s.format(NO_ARGUMENT,
                                 "",
                                 **colors)
            else:
                for arg in vars(args):
                    #if getattr(args, arg, None) is None:
                    #    continue
                    s = "{line}|{argname}{:>"+str(self.max_argname_length)+"}"
                    s += " : {value}{:<"+str(self.max_value_length)+"} {line}|"
                    s += "\n"
                    reps += s.format(arg, str(getattr(args, arg, None)), **colors)
            reps += "{line}o{}o{normal}\n\n".format('-'*(total_line_length),
                                                    **colors)
        fp.write(reps)
        return fp

    def jsonify(self):
        ret = {"args": self.args, "groups": []}
        for group_title in self.arg_groups:
            args = self.arg_groups[group_title]
            d = {'group_title': group_title}
            for arg in vars(args):
                d[arg] = getattr(args, arg, None)
            ret['groups'].append(d)
        return ret
