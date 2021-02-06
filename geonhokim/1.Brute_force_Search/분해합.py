class solution:
    def generator(self, generator_num: int) -> int:
        if generator_num == 1:
            return None

        exp = 1
        generated_num = generator_num

        while generator_num > exp:
            generated_num += generator_num // exp % 10
            exp *= 10
            
        return generated_num

    def brute_force(self, num: int) -> int:
        
        for generator_num in range(1, num):
            if num == self.generator(generator_num):
                return generator_num
        return 0



sol = solution()

num = int(input())

print(sol.brute_force(num))
