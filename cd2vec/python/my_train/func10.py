 def test_cannot_specify_both_producer_and_type(self):
        schema = Schema()
        with self.assertRaises(TypeError):
            schema.define_column('A', producer='my_producer', type='int')