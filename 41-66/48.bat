@echo off
for %%x in (c: g: d: e: f: h:) do (echo program przeszukuje dysk %%x  dir %1 /s /p /b)