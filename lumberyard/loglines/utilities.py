import diff_match_patch as dmp_module


class PrettyDiffMatchPatch(dmp_module.diff_match_patch):

    def diff_prettyHtml(self, diffs):
        html = []
        for (op, data) in diffs:
            text = (data.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '&para;<br>'))
            if op == self.DIFF_INSERT:
                html.append('<span class="text-success">%s</span>' % text)
            elif op == self.DIFF_DELETE:
                html.append('<del class="text-danger">%s</del>' % text)
            elif op == self.DIFF_EQUAL:
                html.append('<span>%s</span>' % text)
        return ''.join(html)
