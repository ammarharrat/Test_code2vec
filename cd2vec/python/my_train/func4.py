  def test_can_specify_header_visibility(self):
        schema = Schema(show_header=False)
        self.assertFalse(schema.show_header)