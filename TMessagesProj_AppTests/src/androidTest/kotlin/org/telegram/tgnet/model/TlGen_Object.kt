package org.tajgram.tgnet.model

import org.tajgram.tgnet.OutputSerializedData

public interface TlGen_Object {
    fun serializeToStream(stream: OutputSerializedData)
}