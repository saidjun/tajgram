package org.tajgram.ui;

import android.content.Context;
import android.view.View;
import android.widget.FrameLayout;

import org.tajgram.ui.ActionBar.BaseFragment;
import org.tajgram.ui.Components.SizeNotifierFrameLayout;

public class EmptyBaseFragment extends BaseFragment {

    @Override
    public View createView(Context context) {
        return fragmentView = new SizeNotifierFrameLayout(context);
    }

}
