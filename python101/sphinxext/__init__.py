# -*- coding: utf-8 -*-
import os
import re

from docutils.utils import relative_path
from sphinx.roles import XRefRole
from sphinx import addnodes

from .. import __version__


class inject_download_css_class(XRefRole.innernodeclass):

    def __init__(self, *args, **kwargs):
        classes = kwargs.get('classes', [])
        classes.append('download')
        kwargs['classes'] = classes
        super(inject_download_css_class, self).__init__(*args, **kwargs)


def visit_inject_download_css_class(self, node):
    getattr(self, 'visit_' + XRefRole.innernodeclass.__name__)(node)


def depart_inject_download_css_class(self, node):
    getattr(self, 'depart_' + XRefRole.innernodeclass.__name__)(node)


class ExerciseRefRole(XRefRole):
    solution_re = re.compile(
        r'#\s+?begin\s+?solution.*?#\s+?end\s+?solution', re.DOTALL)

    def __init__(self, *args, **kwargs):
        self.srcdir = kwargs.pop('srcdir')
        self.doctreedir = kwargs.pop('doctreedir')
        self.exercises_dir = kwargs.pop('exercises_dir')
        super(ExerciseRefRole, self).__init__(*args, **kwargs)

    def result_nodes(self, document, env, node, is_ref):
        file_path = os.path.join(self.srcdir, node['reftarget'].lstrip('/'))
        file_name = os.path.basename(file_path)
        with open(file_path, 'r') as f:
            content = f.read()

        exercise_content = self.solution_re.sub('', content)

        exercise_path = os.path.join(self.exercises_dir, file_name)
        with open(exercise_path, 'w') as f:
            f.write(exercise_content)

        node['reftarget'] = os.path.join(
            '/', relative_path(self.srcdir, exercise_path))

        return [node], []


class SolutionRefRole(XRefRole):
    begin_solution_re = re.compile(r'\s*#\s+?begin\s+?solution')
    end_solution_re = re.compile(r'\s*#\s+?end\s+?solution')

    def __init__(self, *args, **kwargs):
        self.srcdir = kwargs.pop('srcdir')
        self.doctreedir = kwargs.pop('doctreedir')
        self.solutions_dir = kwargs.pop('solutions_dir')
        super(SolutionRefRole, self).__init__(*args, **kwargs)

    def result_nodes(self, document, env, node, is_ref):
        file_path = os.path.join(self.srcdir, node['reftarget'].lstrip('/'))
        file_name = os.path.basename(file_path)
        with open(file_path, 'r') as f:
            content = f.read()

        solution_content = self.end_solution_re.sub(
            '', self.begin_solution_re.sub('', content))

        s_file_name = file_name.split('.')
        new_filename = (
            s_file_name[0] + '_solution.' + '.'.join(s_file_name[1:]))
        solution_path = os.path.join(self.solutions_dir, new_filename)
        with open(solution_path, 'w') as f:
            f.write(solution_content)

        node['reftarget'] = os.path.join(
            '/', relative_path(self.srcdir, solution_path))

        return [node], []


def setup(app):
    srcdir = os.path.abspath(app.srcdir)
    doctreedir = os.path.abspath(os.path.dirname(app.doctreedir))

    exercises_dir = os.path.join(doctreedir, 'exercises')
    if not os.path.exists(exercises_dir):
        os.makedirs(exercises_dir)

    solutions_dir = os.path.join(doctreedir, 'solutions')
    if not os.path.exists(solutions_dir):
        os.makedirs(solutions_dir)

    exercise_reference_role = ExerciseRefRole(
        nodeclass=addnodes.download_reference,
        innernodeclass=inject_download_css_class,
        srcdir=srcdir,
        doctreedir=doctreedir,
        exercises_dir=exercises_dir)

    solution_reference_role = SolutionRefRole(
        nodeclass=addnodes.download_reference,
        innernodeclass=inject_download_css_class,
        srcdir=srcdir,
        doctreedir=doctreedir,
        solutions_dir=solutions_dir)

    app.add_node(
        inject_download_css_class,
        html=(
            visit_inject_download_css_class,
            depart_inject_download_css_class))
    app.add_role('exercise', exercise_reference_role)
    app.add_role('solution', solution_reference_role)
    metadata = {
        'version': __version__,
        'parallel_read_safe': False,
        'parallel_write_safe': False
    }
    return metadata
