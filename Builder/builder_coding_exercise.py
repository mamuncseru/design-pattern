


class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = []

    
    def add_field(self, type, name):
        self.fields.append((type, name))
        return self

    def __str__(self):
        lines = []
        lines.append(f'class {self.root_name}:')
        lines.append('    def __init__(self):')
        for type, name in self.fields:
            lines.append(f'        self.{type} = {name}')

        return '\n'.join(lines)

cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
# cb.add_field('name', '""')
# cb.add_field('age', '0')
print(cb)

