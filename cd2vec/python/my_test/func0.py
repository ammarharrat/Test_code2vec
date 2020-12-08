def test_must_specify_producer_or_type(self):
        schema = Schema()
        with self.assertRaises(TypeError):
            schema.define_column('A')

        with self.assertRaises(TypeError):
            schema.define_column('A', config={'a': 1})