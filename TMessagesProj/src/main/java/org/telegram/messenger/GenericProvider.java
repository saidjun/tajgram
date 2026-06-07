package org.tajgram.messenger;

public interface GenericProvider<F, T> {
    T provide(F obj);
}
