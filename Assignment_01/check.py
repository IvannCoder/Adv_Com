from ac import AirConditioner

results = []
def check(name, fn):
    try:
        fn(); results.append((name, True, ""))
    except AssertionError as e:
        results.append((name, False, str(e) or "assertion failed"))
    except Exception as e:
        results.append((name, False, f"{type(e).__name__}: {e}"[:80]))

def c1():
    ac = AirConditioner("Daikin", "Bedroom")
    assert "Bedroom" in str(ac)
check("1. Builds and __str__ works", c1)

def c2():
    ac = AirConditioner("Daikin", "Bedroom"); ac.temperature = 22
    assert ac.temperature == 22
check("2. A valid temperature is stored", c2)

def c3():
    ac = AirConditioner("Daikin", "Bedroom")
    ac.temperature = 22; assert ac.is_energy_saving is False
    ac.temperature = 26; assert ac.is_energy_saving is True
check("3. is_energy_saving reflects the CURRENT temperature", c3)

def c4():
    ac = AirConditioner("Daikin", "Bedroom")
    for bad in (5, 40):
        try: ac.temperature = bad; assert False, f"accepted {bad}"
        except ValueError: pass
check("4. Out-of-range temperature is rejected", c4)

def c5():
    try: AirConditioner("LG", "Office", temperature=99); assert False, "ctor accepted 99"
    except ValueError: pass
check("5. The constructor also rejects bad values", c5)

def c6():
    ac = AirConditioner("Daikin", "Bedroom", temperature=16)
    ac.cooler(); assert ac.temperature == 16
check("6. cooler() never drops below the minimum", c6)

passed = sum(1 for _, ok, _ in results if ok)
for name, ok, msg in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"   -> {msg}" if not ok else ""))
print(f"\n{passed}/{len(results)} checks passing")
