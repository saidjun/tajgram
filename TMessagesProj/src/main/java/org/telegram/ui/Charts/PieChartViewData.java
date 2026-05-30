package org.tajgram.ui.Charts;

import android.animation.Animator;

import org.tajgram.ui.Charts.data.ChartData;
import org.tajgram.ui.Charts.view_data.StackLinearViewData;

public class PieChartViewData extends StackLinearViewData {

    float selectionA;
    float drawingPart;
    Animator animator;

    public PieChartViewData(ChartData.Line line) {
        super(line);
    }
}
