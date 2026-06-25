def on_menu_pressed():
    pass
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

music.play(music.create_song(hex("""
        0078000408020701001c000f05001202c102c20100040500280000006400280003140006020004240008000c0001291400180001292000240001292c00300001293400380001293c004000012903001c0001dc00690000045e0100040000000000000000000005640001040003060008000c00012504001c00100500640000041e000004000000000000000000000000000a040004250000000400012504000800010d0c001000020d2510001400010c1400180001251c002000012405001c000f0a006400f4010a0000040000000000000000000000000000000002430004000800011608000c0001120c00100001141000140002111614001800011618001c0001161c00200001122400280001122c003000011634003800011638003c00011206001c00010a006400f4016400000400000000000000000000000000000000022b000400080001270c00100001291c002000012a24002800020a242c003000010830003400010c38003c00010807001c00020a006400f4016400000400000000000000000000000000000000032b0004000800010a08000c00010810001400010624002800010d2c003000020d1234003800011138003c00010d09010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8003100000001000214040400050001040800090001040c000d0001041000110001041400150001041800190001041c001d000104
        """)),
    music.PlaybackMode.IN_BACKGROUND)
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff88888888888888888888888888888888888888888888888888888888888888777888888888888888888888
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff88888888888888888888877777777777777777777777778888877777777777777777777777777777778888888
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff88888888888888888777777788888888877888888888777777777787777777777788888888888888888877778888
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8888888888888877777778888888887777788887777777877777777777778888888877777777777777777788888888
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff88888888888777777877777777777777777777777777777777888877888777777777777778887777888888888888888
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8888888887777777777788888777777877777777777788887777777777777777778888888887777788777888888888888
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff88888777777777778888877777888777777777777777777777777787777777777788888888888888877888777888888888
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8888777777777888887777788877777777777888888888888888777778888888888877777777888888888788888777888878
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff888887777777888888778877777777777887777777777778888888777777777777777777788788778888888878888888777788
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffff7788888877888888877777777787777877778888877888777777777878888888778888877877888887788888878888888778778
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffff78788888888887777788877787777777788888877777777888888777788888877788887788887778888877888878888877888888
    fffffffffffffffffffffffffffffffffffffffffffffffffffffff787878878877777778877777777777777777777777788888888888777777777787888778888878887788888778788777788888888
    ffffffffffffffffffffffffffffffffffffffffffffffffffffff7887787778788877877777777777788888887888787888888888877787888777777777888877778888877888887777877788888888
    ffffffffffffffffffffffffffffffffffffffffffffffffffff8788778777887887888787777777777778888778878878777777777877788777777887877777887888888887777778787f7888888888
    fffffffffffffffffffffffffffffffffffffffffffffffffff7788777777887778877777777777887778887778877778787788777777888777778877888878877778888888887788877f78888888888
    fffffffffffffffffffffffffffffffffffffffffffffffff878877877787877887777777887878777878877888778777778777787878877777788788887788878887777777778877777788888878888
    ffffffffffffffffffffffffffffffffffffffffffffffff8788787778777778887777788777777888877778877887777787778778788777778877888878888777777777777888877f78888888778888
    fffffffffffffffffffffffffffffffffffffffffffffff878877777877787887777888878777888887778877788777887778778877777777887ff888788888778887787788888787788888777888888
    ffffffffffffffffffffffffffffffffffffffffffffff878877877877777887778888777778888877788778877777877777788877777778877.f8887888877888777778888887778888877788888f88
    fffffffffffffffffffffffffffffffffffffffffffff87887787787777887778888777777888777788778887777777777788877777778887f.f88878888778877777888888777f8888778778888f888
    ffffffffffffffffffffffffffffffffffffffffffff878877877877777877788877777778887877877788877777777778888777777788f7ddf8887888777887787788888877ff88887887788888f888
    fffffffffffffffffffffffffffffffffffffffffff87887777787777787778877777778887787777788887777777777888777777788877ddf888788878787778778888887fff88877877788888f.888
    ffffffffffffffffffffffffffffffffffffffffff88787777787777777788877787778887877777788877778877787887777778788f7ddddf88878878787778778777877f.f8887887778888ff88ddd
    fffffffffffffffffffffffffffffffffffffffff88787777788778777788877887778877777777fff87777877788778777787878877ddddf88878777777787777778877f.f8887887777778fddddddd
    fffffffffffffffffffffffffffffffffffffffff878778777877877778877888777877777777877f77777777888778777777878f7dddddf8887878787778787778877fddf88878777788878fddddddd
    ffffffffffffffffffffffffffffffffffffffff878777777877777788878888777777777777877778787788788777777778878f7dddddf8887878787778777788877dddf88778777888878fdddddddd
    fffffffffffffffffffffffffffffffffffffff87887777787777778877888877777777777787777777778878877777778877877dddddf8887778777778777788887dddf88787777888878fddddddddd
    ffffffffffffffffffffffffffffffffffffff88787777787777778877888877777777777777777787778878877877788878f7ddddddf888878877777777788888f7ddf88787778788878fdddddddddd
    ffffffffffffffffffffffffffffffffffffff8787777787777788877888877777777777777.7788777887887777778887877dddddddf88878877778777888888fdddf8877777778877ffddddddddddd
    fffffffffffffffffffffffffffffffffffff8787778777777788777888877777877877777f7f88778788777777788887f7ddddddddf88878877778777888888fdddf8877778788878fddddddddddddd
    fffffffffffffffffffffffffffffffffffff878778777777788787888777877877877777fdf8877778877777778888777ddddddddf88877877877777888888fddddf877878878778fdddddddddddddd
    fffffffffffffffffffffffffffffffffffff7877777777667878f887778777777877777fddf77777887777777888877dddddddddf88877877877778888888fddddf87777887878ffddddddddddddddd
    ffffffffffffffffffffffffffffffffffff78777877776668777f77877777777777777fddd7877878777778788887ddddddddddf88877877877778888888fddddf87877887778fddddddddddddddddd
    fffffffffffffffffffffffffffffffffff878768777776667ff8f8877777777777777dddd787787777777878888fddddddddddf8888777787777888888ffddddf87877887788fdddddddddddddddddd
    fffffffffffffffffffffffffffffff666666666666666666ff8f8877777777877777fddd78878778777787888ffddddddddddf8888777787777888778fdddddf87877887788fddddddddddddddddddd
    ffffffffffffffffffffffffff66666fff787766667677666f888877777777877777fdd777878778777787888fdddddddddddf8888777787778887787fdddddf8777888778ffdddddddddddddddddddd
    fffffffffff6fffffffff66666f6666666667766666667666888877777778777777fdd7.f87777877778788ffdddddddddddf8888787787878877887fdddddf8777788778fdddddddddddddddddddddd
    ffffffffffff66666666666666666fff6666876666766f66688887777778777777fdd7.f8777878777878ffdddddddddddddf888787777778778887fddddddf787788788fddddddddddddddddddddddd
    fffffffffff666666666666f66666666667676666676f66668887878788777777fdd7..f878878778778fddddddddddddddf888877777777788887dddddddf77778778ffdddddddddddddddddddddddd
    fffffffff66666f66fff66666666666f666667666666f6666887878788777877fdd7..f777878778778fddddddddddddddf888877877777888887dddddddf87887778fdddddddddddddddddddddddddd
    fffffffff6f666f6666666666666666f666667666666.666687878788777877fdd7..f77788777877ffddfdddddddddddf888877777777888877ddddddddf8887778fddddddddddddddddddddddddddd
    fffffffff6f6f6666f666f6666666667666667666666.66667877788777877fdd7...77778777877fdddfdddddddddddf88888777778788887dddddddddf888887ffdddddddddddddddddddddddddddd
    fffffffff6f6f666666666666666666666666666666666666777788777877fdd7..777878877877fddddfdddddddddddf88887778787888f7dddddddddf888787fdddddddddddddddddddddddddddddd
    fffffffff6f6f6666f666f66666666666666666666666666687788777877fdd7777f8778878777fdddddfddddddddddf8888777778788877ddddddddddf88787dddddddddddddddddddddddddddddddd
    fffffffff6ff66666f666f66666f6667666666666666f66667788777877fddddddf8787877787fddddddfdddddddddf888877777778887dddddddddddf88787ddddddddddddddddddddddddddddddddd
    ffffffffff6ff6666f666f66666f666766666666666666666788777877fddddddf8787877787ddddddddfdddddddddf88877877788887ddddddddddddf8777dddddddddddddddddddddddddddddddddd
    ffffffffff6ff6666f666f66666f666.6666666666666666678777777fdddddddf878777777dddddddddfddddddddf88777777788877dddddddddddddf77fddddddddddfdddddddddddddddddddddddd
    ffffffffff66ff66f6666666666f6667666666666666666668777777fdddddddf8787777777dddddddddfdddddddf8877777788887fddddddddddddddf7ddddddddddddddddddddddddddddddddddddd
    ffffffffffd6dd6dd66666666666666.66666666666666666777777fddddddddf878787777ddddddddddfdddddddf877877788887fdddddddddddddddddddddddddddddddddddddddddddddddddddddd
    fffffffffddddddddd6d66666666666.6666666666666666677777fddddddddf878787777dddddddddddfddddddf877877788877fddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffdddfdfdfddd6666666666666666666666666666666677778fddddddddf87777777ddddddddddddfdddddf87887778887ffdddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffdfffdfdfdddff6666666676666666666666666666667778fddddddddf87777777dddddddddddddfddddd77877778887fdddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffdfffdfdfddddf666666666666666666666666666666778fdddddddddf8777777ddddddddddddddfdddd78778778887fddddddddddddfdddddddddddddddddddddddddddddddddddddddddddddd
    fffffffdffdfddddddd66666666666666666666666666666687fdddddddddf8787877dddddddddddddddfddd77788778877fdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    fffffffdfddfddddddd66666666666666f6666666666666667fdddddddddf8777777ddddddddddddddddfd77788877887fdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffffdddfddddddd666666666666666666666666666666fdddddddddf8777877dddddddddddddddddfdf888887887dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffffdddfddddddd6f6666666666666666666666666666ddddddddddf877ff.7dddddddddddddddddff8888878fffffffffffdddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffffdddfddddddd6f66f6666666666666666666666666dddddddddff77f..7ddddddddddddddddd7fffffffffffffffffffffff1fffffddddddddddddddddddddddddddddddddddddddddddfffff
    ffffffdfdddfddddddd6f66d666666666f666666666666666ddddddddf877f..7dddddddddddddddff77ffffffff1fff11ffffffff11ffff.fffddddddddddddddddddddddddddddddddddffffff.1..
    ffffffdfdddfddddddd6f666666666666f666666666666666ddddddddf877..7ddddddddddddddffff77ffffffff1ddd11ffff1ff1f1.fffffffdddddddddddddddddddddddddddddddfffff7.f.11..
    ffffffdfdddfddddddd6f6666666f66666666666666666666ddddddddf8f777dddddddddddddfffff.77ffff7ddd1d1d11dddd1d1f1fffffffffddddddddddddddddddddddddddddddff.ff7.7f.11..
    ffffffdfdddfddddddd6f6666666f66666666666666666666dddddddfffd7dddddddddddddffff.fff77ff.f7dddd11d11ddd111df1ddddfffffdddddddddddddddddddddddddddddfffff7..7.f711.
    ffffffdfddfddddddfd6f66f6666f6666666666666666666ffddddddddddddddddddddddffffffffff777f..7dddd11111dd11111d1ddddddddfdddddddddddddddddddddddddddffdfff.7..7.7711.
    ffffffdfddfddddddfd6f66f6666f66666666666666666666ffdddddddddddddddddddffff.fffffff777f777fddd111d1d11111d1ddddddddddddddddddddddddddddddddddddddddddf.77.77f7111
    ffffffdfddfddddddddd666f6666666666666666666666666f.fdddddddddddddddddf.f.fffff.fff777f777fdd1111d11d11d1d1dddddddddddddddddddddddddddddddddddddddddf..77.777.11.
    ffffffdfdddddfdddddd66666666666666666666666666666ff.fdddddddddddddddfdfff.ff..ff.f777f777.fd1111d11d1d1dd1dddddddddddddddddddddddddddddddddddddddddf..77.77f.11.
    ffffffdfdddddfdddddd6f666666ff6666666666666666666fff.fddddddddddddffdddf.fff..f77f777f777.fd111111d11d1d1ddddddddddddddddddddddddddddddddddddddddddf..77.77f1111
    ffffffdfdfdfdfdddddd6d6666666666666666666666666666f.f.fddddddddddfddddf.ff.f.f.77f777f777.fd1d11111111d1fddddddddddddddddddddddddddddddddddddddddddf.777.7.f1111
    ffffffdddfdfdfddddddd66666666f66666666666666f66f66ff.f.fddddddddfddddf.ff..ff..f7f777f777.fd1d1111111d1ffddddddddddddddddddddddddddddddddddddddddddf.77777f.1111
    fffffffddfffdfddddfdd6666666ff66ff666f6f66666666.66ffffffdddddddfdddf..f...ff..fff777f777.fd11111111d1dfdddddddddddddddddddddddddddddddddddddddddddf.7777.f.11.1
    fffffffdffffdfddddfddd6666f66666ff666666666ff66ff66f..f.fdddddddddddf..f...ff..f.f.77f777.fd1111111d1dfddddddddddddddddddddddddddddddddddddddddddddf.7777f..11..
    fffffffdffffdfdddfddddf66ffff6f666666f66f66f6f6.ff6f...fffdddddddddf...f..ff..f.ff.77f77..fd11111111dfddddddddddddddddddddddddddddddddddddddddffdddf.77.7...11..
    fffffffddfffdfddffddfdf66ffff6f6fff66f66d6d6f.6fff66ff.ffffddd1dddf....ff.ff..f.ff.77f....fd11111111ffddddfffdddddddddddddddddddddddddddddddddfffddf..7.7....1..
    fffffffddfffdfdfffddfdf66ffddd66ddd6d66d6f66ff6fff66f.fffffffdddddf.....ffffffffff.77f.7.fddd111111fddddfffdddddddddddddddddddddddddddddddddddfdddddf.7f.f..11ff
    fffffffddfffdffffffdddd66ddffff666666f6666ffdfff.f66ff..ffff.fddddf.....fff.....fff7777.fdddd11d11..ffffffddddddddddddddddddddddddddddddddddddfffdddf.f..fff1dff
    fffffffddfffdfffdfddfddf6fddfddd11fdd66f1fffdfdddd66f.ff..f.f.fdddf...ff........ff777f..fddddd1f1..f.fffdddddddddddddddddddddddddddddddddddddddddffffffffdddddff
    fffffffddfffdfddddddfddd6dddddddddddddddddddddf.fdd66fddf..fff.fdddfffff.........ff7.fffddddff1.fff.fddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    fffffffddfffdddfdfdddddddddffff1dddddddd1dfdffdddf.66fdddf...fffffddddddffff....ff7fffffffffffff..ffdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    fffffffdddddfffddfddddddddddddddddddddddddddddddff.6f6ddddff..fff.fddddddfffffff.f7ff.f...ff..ffffdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffffdddfffddfdddddddddddddddddddddddddddddfdff.f66fdddddf...ffffddddddddfff...77f.f..fffffdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffffdddfffddddddddddddddddddddddddddffdfffffdd.f66fddddddf...ffffffffffff.fffffffffff..f.fdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    fffffffffddffdddddddddddddddddddddddffddffdfffffffd.f6ffddddddff..f.ffff.f..fff...fff.f....f.fddddddddddddddddd3dddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffffffdffdddddddddddddddddddddddddddddddffffffdddfffddddddddff.f.ffffff..fff....fff...f..fdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffffffdffddddddddddddddddddddddddddddddddddddd.df.fffdddddddddffff.fffffff.fff....fffff..fdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffffffddddddddddddddddddddddddddddddddddddddddddd.f.fdddddddddddfffffffff.ffffff..f..fff.fdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    fffffffffddfd6ddddddddddddddddddddddddddddddddddddd.d..fffffdddddddddffffffffff.fffff.ff.f..ffdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffffffdddfdddddfddddddddddddddddddddddddddddddddd..fff..fddddddddddff.ff.fff..f.fffff....ffddddddddddddddddddddddddddddddddddddddddddddddddddddddddfdddddddd
    ffffffffffdddfdddfdfdddddddddddddddddddddddddddddddddff..f...fdddddddddddff.f.ffff.f..fff....f.ffddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffffffdddfdddfdfdddddddddddddddddddddddddddddddddffff.f...fdffffffdddfffff..fffff.f.ff...f...fddddfffddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    ffffffffffdddddddfdfdddddddddddddddddddddddddddddddddffffffffffffffdddddff..ffff.ff.ff.f.fff.f....ffdf...fdddddddddddddddddddddddddddddddddddddddddddddddddddddd
    fffffffffffdddddddddddddddddddddddddddddddddddddddddf.fffffffffffffffffff.ffffffff.ffff.f.ffff......f....fdddddddddddddddddddddddddddddddddddddddddddddddddddddd
    fffffffffffdfdddddddddddddddddddddddddddddddddddddddf.ffffffffffffffffff.fffffffffff.fffff.fffff....ff....fddddddddddddddddddddddddddddddddddddddddddddddddddffd
    fffffffffffdfdddddddddddddddddddddddddddddddddddddddfffffffffffffffffff.fffffffffffffffffff.ff..ff..ffff..fddddddddddddddddddddddddddddddddddddddddddddddddddffd
    fffffffffffdddddddfdddddddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffff.fffff.fff...ffffffffffffdddddddddddddddddddddddddddddddddddddddddddddddffd
    fffffffffffdddddddfddddddddddddddddddddddddddddddddffffffffffffffffffffffffffffffffffff.fffff.ffffffff..ff.fddfdddddddddddddddddddddddddddddddddddddddddddfffffd
    fffffffffffdddddddfddddddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffffffff..ffff.fffffffff.fffddddddddddddddddddddddddddddddddddddddddddddddfffffd
    fffffffffffdddddddfddddddddddddddddddddddddddddddddffffffffffffffffffffffffffffffffffff.f..ffff.ffffffffff..fffddddddddddddddddddddddddddddddddddddddddddffffffd
    fffffffffffdddddddfddddddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffffffff.ffffffdffddffddffff.fdddffffffffffffffddddddddddddddddddddddddff.fffffd
    ffffffffffdfddddddfddddddddddddddddddddddddddddddddffffffffffffffff1ff1fff11fffffffffff.fffffddfffffd.fddddffffff..............fffdddddddddddddddddddff.fffffffd
    ffffffffffdfdfddddfddfdddddddddddddddddddddddddddddffffffffffffffff11111f111fffffffffff....ddffff88ffffddffffffff.............ffffffffffdddddddffffffffffffffffd
    ffffffffffdfdfddddfddfdddddddddddddddddddddddddddddfffffffffffffff111111111ffffffffffff....dffff8f8ffffffddddffffffffffffffffffffffffffffffffffffffffff..f.ffffd
    ffffffffffdfdfdddddddfdddddddddddddddddddddddddddddffffffffffffffff1f111111ffffffffffff..ffffff8ff8ffffffddddddddffff.......f...ff.....f...ffffddf..f....f.ffffd
    ffffffffffdfdfdddfdddddddddddddddddddddddddddddddddffffffffffffffff1111111fffffffffffff..ffff88ff77f.fffffddddddddffffff.....ffffffffffffffdddddffff....ff.ffffd
    ffffffffffdddddddfdddddddddddddddddddddddddddddddddffffffffffffffff11111111fffffffffffffffff878.87ff7fff.fdffddddddf..fff..............fddddddddddf.....ff.ffffd
    fffffffffdfddddddfdddddddddddddddddddddddddddddddddffffffffffffffff111111111fffffffffffffff8878877.f7fffffddddddddddff..fffffff.......ffdddddddddddf....ff.fffff
    fffffffffdfddddddfdfdfdddddddddddddddddddddddddddddfffffffffffffffff111111f1ffffffffffffff8878..77.77fffffddddddddddddfffffddddfffffffddddddddddddddf...ff.fffff
    fffffffffdfddddddfdddfdddddddddddddddddddddddddddddffffffffffffffff11f1111f1ffffffffffffff887..77777.ffffffdddddddddddddddddddddddddddddddddddddddff....ff.fffff
    fffffffffdfddddddddddfddddddddddddddddddddddfddddddfffffffffffffffffff11f1f1fffffffffffff8877..777.7.ffffffdddddddddddddddddddddddddddddddddddddddddff..ff.fffff
    fffffffffdfddddddddfddddddddddddddddddddddddddddddfffffffffffffffffffff1f11ffffffffffff.88877f777.77.ffffdfdddddddddddddddddddddddddddddddddddddddddddffff.fffff
    fffffffffdfdddddfddfdddddddddddddd1dddddddddddddddfffffffffffffffffffff1ff1ffffffffffff888777f77.777.ffffdfdddddddddddddddddddddddddddddddddddddddddddddffffffff
    fffffffffdfddddffdfdddddddddddddddddddddddddddddddffffffffffffffffffffff1fffffffffffff8887777777.77ffffffffdddddddddddddddddddddddddddddddddddddddddddddff.fffff
    fffffffffdfddddffdfdddddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffffff88887777777.77ffffffddfddddddddddddddddddddddddddddddffddddddddddddff.fffff
    fffffffffdfddddfddffddddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffffff88887777777777.ffffffdfddddddddddddddddddddddddddddddddddddddddddddff.ff.ff
    fffffffffdffdddfffffddddddddddddddddddddddddddddddffffffffffffffffffffffffffffffffff88888777.777.7ffffffffdfddddddddddddddddddddddddddddddddddddddddddddff.ff.ff
    fffffffffdffdfffffffdfddddddddddddddddddddddddddddffffffffffffffffffffffffffffffffff88887777777..f.fffffffdfddddddddddddddddddddddddddddddddddddddddddddfffff.ff
    fffffffffdfffffffffffdddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffff8888.777.777f.ffffffffff.fdddddddddddddddddddddddddddddddddddddddddddfffff.ff
    fffffffffdffffffdddddddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffff88888.777.77..f.fffffffff.fdddddddddddddddddddddddddddddddddddddddddddfffff.ff
    fffffffffdffddddfffffddddddddddddddddddddddddddddfffffffffffffffffffffffffffffffff8888ff777.77f.f.fffffffffffdddddddddddddddddddddddddddddddfffddfddddddfffff.ff
    fffffffffdddffffffffffdddddddddddddddddddddddddddfffffffffffffffffffffffffffffffff.88.....7777fff.fffffffffffddddddddddddddddddddddddddddddddddddddddddddffff.ff
    ffffffffffffffffffffffdddddddddddddddddddddddddddffffffffffffffffffffffffffffffffff8......7.7.ffffffff..fffffdddddddddddddddddddddddddddddddddddddddddddddfff.f.
    """))
myMenu = miniMenu.create_menu(miniMenu.create_menu_item("Play"),
    miniMenu.create_menu_item("Quit"))
achievements.create("You opened the game",
    1,
    "Achevment",
    img("""
        . . . . . . . . . . b 5 b . . .
        . . . . . . . . . b 5 b . . . .
        . . . . . . . . . b c . . . . .
        . . . . . . b b b b b b . . . .
        . . . . . b b 5 5 5 5 5 b . . .
        . . . . b b 5 d 1 f 5 5 d f . .
        . . . . b 5 5 1 f f 5 d 4 c . .
        . . . . b 5 5 d f b d d 4 4 . .
        b d d d b b d 5 5 5 4 4 4 4 4 b
        b b d 5 5 5 b 5 5 4 4 4 4 4 b .
        b d c 5 5 5 5 d 5 5 5 5 5 b . .
        c d d c d 5 5 b 5 5 5 5 5 5 b .
        c b d d c c b 5 5 5 5 5 5 5 b .
        . c d d d d d d 5 5 5 5 5 d b .
        . . c b d d d d d 5 5 5 b b . .
        . . . c c c c c c c c b b . . .
        """))
miniMenu.create_menu_item("Play").set_disabled(True)

def on_selection_changed(selection, selectedIndex):
    pass
miniMenu.on_selection_changed(myMenu, on_selection_changed)

adventure.add_image_to_text_log(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    """))