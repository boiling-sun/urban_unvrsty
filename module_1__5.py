def main():
    immutable_var = 'foo', 0, 3.5, ['bar'], None, True
    try:
         # >>> "Объясните, почему нельзя изменить значения элементов кортежа."
        immutable_var[0] = 'baz'
    except TypeError:
        print('(1) According to data model sequences are distinguished by their mutability.')
        print('An object of an immutable sequence type cannot change once it is created.'
              + 'They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.', end='\n\n')
        print(f'"immutable_var" reffers to {type(immutable_var)} which is immutable type.', end='\n\n')
    finally:
        print('Tuple may contain references to other objects, these other objects may be mutable and may be changed as follows:')
        print(f'{immutable_var} --> ', end='')
        immutable_var[3].append('baz')
        print(f'{immutable_var}', end='\n\n')

    mutable_list = ['foobar', 2, 1, None]
    print(f'(2) Mutable list before: {mutable_list}')
    mutable_list[0] = 'baz'
    print(f'Mutable list after: {mutable_list}')

if __name__ == '__main__':
    main()
