# Define the initial expression
class OptimizeCode:
    def optimize_expression(self, expr, type = None):
        if isinstance(expr, (float, int)):
            if (type == 'int'):
                return int(expr)
            else:
                return float(expr)
        if (isinstance(expr, tuple)):
            op, left, right = expr
        else:
            return str(expr)
        if isinstance(left, tuple):
            left = self.optimize_expression(left, type)
        if isinstance(right, tuple):
            right = self.optimize_expression(right, type)
        if isinstance(left, (float, int)) and isinstance(right, (float, int)):
            return eval(f'{left} {op} {right}')
        
        if (isinstance(left, (float, int))):
            if (type == 'int'):
                left = int(left)
            else:
                left = float(left)
        
        if (isinstance(right, (float, int))):
            if (type == 'int'):
                right = int(right)
            else:
                right = float(right)

        return f'({left} {op} {right})'
