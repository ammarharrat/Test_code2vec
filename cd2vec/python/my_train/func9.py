def test_str(self):
        schema = Schema()
        schema.add_producer('my_producer', type='int')
        schema.define_column('A', producer='my_producer')
        schema.define_column('B', producer='my_producer')
        str_regex = re.compile(r'''
            Schema\(
            \s*columns=\[[^]]+\],
            \s*producers=\{my_producer:\s*\{'type':\s'int',\s'config':\s\{\}\}\},
            \s*transformers=(\{'name':\s'(A|B)',\s*'transformer':\s<feanor\.schema\.ProjectionTransformer\sobject\sat\s\w+>,\s*'inputs':\s\[[^]]+\],\s'outputs':\s\[[^]]+\]\},?\s*)+
            show_header=True\s*
            \)
        ''', re.VERBOSE)
        self.assertRegex(str(schema), str_regex)