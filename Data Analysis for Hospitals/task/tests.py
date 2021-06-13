from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


answers = ['general', 'pregnancy']


class EDATest(StageTest):
    def __init__(self, method: str):
        super().__init__(method)

        self.figures = []

        import matplotlib
        import matplotlib.pyplot as plt
        from matplotlib._pylab_helpers import Gcf
        matplotlib.use("agg")

        def custom_show_func(*args, **kwargs):
            managers = Gcf.get_all_fig_managers()
            for m in managers:
                self.figures.append(m.canvas.figure)
                Gcf.destroy(m.num)

        plt.show = custom_show_func

    def generate(self):
        return [
            TestCase()
        ]

    def check(self, reply, attach):
        if len(self.figures) == 0:
            return CheckResult.wrong(
                'Looks like you didn\'t presented plots using "plt.show()" command')

        lines = [line for line in reply.split('\n') if len(line) > 0]
        if len(lines) != 3:
            return CheckResult.wrong(
                'You should output exactly 3 lines with answer to each question in each line. '
                f'Found {len(lines)} lines')

        if answers[0] not in lines[0]:
            return CheckResult.wrong('The answer to the 1st question is incorrect')

        if answers[1] not in lines[1]:
            return CheckResult.wrong('The answer to the 2nd question is incorrect')

        return CheckResult.correct()


if __name__ == '__main__':
    EDATest('analysis').run_tests()
