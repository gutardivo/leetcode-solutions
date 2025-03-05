def twoSum(nums, target):
    num_map = {}  # Dicionário para armazenar valores e seus índices
    
    for i in range(len(nums)-1):
        complement = target - nums[i]  # O número necessário para formar a soma
        
        if complement in num_map:
            return [num_map[complement], i]  # Retorna os índices dos dois números
        
        num_map[nums[i]] = i  # Armazena o número no dicionário
    
    return []  # Caso não encontre (embora o problema garanta uma solução)

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))