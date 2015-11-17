import urwid
import parser1 as parser

def on_query_change(edit, new_edit_text):
    try:
        if new_edit_text:
            answer.set_text(('query',u"%s" % parser.evaluate(new_edit_text)))
        else:
            answer.set_text(('query',u""))
    except:
        #do nothing here
        print "exception"


def on_exit_clicked(button):
    raise urwid.ExitMainLoop()

palette = [('query', 'default,bold', 'default', 'bold')]

query = urwid.Edit(('query',""))
answer = urwid.Text(u"")
button = urwid.Button(u"Exit")
div = urwid.Divider()
pile = urwid.Pile([query,div,answer,div,button])
top = urwid.Filler(pile, valign='top')

urwid.connect_signal(button,'click',on_exit_clicked)
urwid.connect_signal(query,'change',on_query_change)

urwid.MainLoop(top,palette).run()
