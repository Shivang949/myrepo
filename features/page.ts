import {defineField} from 'sanity'

export const page = ({
    name: 'page',
    title: 'Page',
    type: 'document',
    fields: [
        defineField({
              name: 'title',
              title: 'Title',
              type: 'string',
              validation: Rule => Rule.required().min(3),
            }),
        defineField({
              name: 'subTitle',
              title: 'SubTitle',
              type: 'string',
            }),
        defineField({
              name: 'path',
              title: 'Path',
              type: 'string',
            }),
        defineField({
              name: 'identifier',
              title: 'Identifier',
              type: 'string',
              validation: Rule => Rule.required(),
            }),
        defineField({
              name: 'items',
              title: 'Items',
              type: 'array',
              of: [{type: 'items'}]
            }),
        ],
    })