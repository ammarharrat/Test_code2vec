 def test_can_define_column_configuration(self):
        schema = Schema()
        schema.define_column('A', type='int', config={'a': 10})
        self.assertEqual(('A',), schema.columns)
        self.assertEqual('A', schema.producers[0].name)
        self.assertEqual('int', schema.producers[0].type)
        self.assertEqual({'a': 10}, schema.producers[0].config)