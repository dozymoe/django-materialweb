import { forOwn, omit, pick } from 'lodash';

export function ensurePrimitive(value)
{
    // Catch mobx.observable.box()
    return value && value.get ? value.get() : value;
}

export function ensurePrimitiveProps(props)
{
    let values = {...props};
    forOwn(values, (value, key, object) => object[key] = ensurePrimitive(value));
    return values;
}

export function extract(props, ...fields)
{
    let values = pick(props, fields);
    forOwn(values, (value, key, object) => object[key] = ensurePrimitive(value));
    return [values, omit(props, fields)];
}
