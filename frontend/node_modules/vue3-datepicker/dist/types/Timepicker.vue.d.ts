import { ComputedRef, Ref, PropType } from 'vue';
interface Item {
    value: number;
    date: Date;
    ref: Ref<null | HTMLElement>;
}
declare const _default: import("vue").DefineComponent<{
    selected: {
        type: PropType<Date>;
        required: false;
    };
    pageDate: {
        type: PropType<Date>;
        required: true;
    };
    visible: {
        type: BooleanConstructor;
        required: true;
    };
    disabledTime: {
        type: PropType<{
            dates?: Date[] | undefined;
            predicate?: ((target: Date) => boolean) | undefined;
        }>;
        required: false;
    };
}, {
    hoursListRef: Ref<HTMLElement | null>;
    minutesListRef: Ref<HTMLElement | null>;
    hours: Ref<number>;
    minutes: Ref<number>;
    hoursList: ComputedRef<Item[]>;
    minutesList: ComputedRef<Item[]>;
    padStartZero: (item: number) => string;
    selectMinutes: (item: Item) => void;
    isEnabled: (target: Date) => boolean;
    scroll: () => void;
}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, {
    select: (date: Date) => boolean;
    back: () => true;
}, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<{
    pageDate: Date;
    visible: boolean;
} & {
    selected?: Date | undefined;
    disabledTime?: {
        dates?: Date[] | undefined;
        predicate?: ((target: Date) => boolean) | undefined;
    } | undefined;
}>, {}>;
export default _default;
