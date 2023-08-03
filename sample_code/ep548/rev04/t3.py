

class C:
    def frob(self):
        print('default')

    def do_work(self):
        self.frob()


class D(C):
    def frob(self):
        print('something else')


D().do_work()
