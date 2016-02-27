# automatically generated, do not modify

# namespace: Example

import flatbuffers

class TestSimpleTableWithEnum(object):
    __slots__ = ['_tab']

    # TestSimpleTableWithEnum
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TestSimpleTableWithEnum
    def Color(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 2

def TestSimpleTableWithEnumStart(builder): builder.StartObject(1)
def TestSimpleTableWithEnumAddColor(builder, color): builder.PrependInt8Slot(0, color, 2)
def TestSimpleTableWithEnumEnd(builder): return builder.EndObject()
