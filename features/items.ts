import {defineField, defineType} from 'sanity'

export default defineType({
    name: 'items',
    title: 'Items',
    type: 'object',
    fields: [
        defineField({
            name: 'title',
            title: 'Title',
            type: 'string',
        }),
        defineField({
            name: 'subtitle',
            title: 'Subtitle',
            type: 'string',
        }),
    ]
})