# Django ORM: CRUD Operations

Примеры выполнения базовых операций CRUD (Create, Read, Update, Delete) с использованием Django ORM.

---

## 1. CREATE (Создание)

```python
x = User(name='Ivan')
x.save()
# или
User.objects.create(name='Ivan')
```

## 2. READ (Чтение)
```python
# Получить всех пользователей
User.objects.all()

# Фильтрация пользователей по имени
User.objects.filter(name='Ivan') 

# Получить одного пользователя по ID
User.objects.get(id=5) 

# Перебор всех пользователей и вывод их имен
for user in User.objects.all(): 
    print(i.name)
```

## 3. UPDATE (Обновление)
```python
# Обновление имени конкретного пользователя
x = User.objects.get(id=1)
x.name = 'Max'
x.save()

# Обновление имени нескольких пользователей с использованием filter()
User.objects.filter(id=5).update(name='Max')
```

## 4. DELETE (Удаление)
```python
# Удаление конкретного пользователя по ID
User.objects.get(id=5).delete()
```