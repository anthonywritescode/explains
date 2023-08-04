from typing import override


class C:
    def new_frob(self):
        print('default')

    def do_work(self):
        self.new_frob()


class D(C):
    @override
    def frob(self):
        print('something else')


D().do_work()
