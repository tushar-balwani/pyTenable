from typing import List, Dict

from tenable.ad.widget.schema import WidgetSchema, WidgetOptionSchema
from tenable.base.endpoint import APIEndpoint


class WidgetsAPI(APIEndpoint):
    _path = 'dashboards'
    _schema = WidgetSchema()

    def list(self, dashboard_id: str) -> List[Dict]:
        '''
        Retrieve all widgets

        Returns:
            list:
                The list of widget objects

        Examples:

            >>> tad.widgets.list()
        '''
        return self._get(f"{dashboard_id}/widgets")

    def create(self,
               dashboard_id: str,
               pos_x: int,
               pos_y: int,
               width: int,
               height: int,
               title: str) -> List[Dict]:
        '''
        Create a new widget

        Args:
            dashboard_id:
                The dashboard instance identifier.
            pos_x:
                x-axis position for widget.
            pos_y:
                y-axis position for widget.
            width:
                width of widget.
            height:
                height of widget.
            title:
                title for widget.


        Returns:
            list[dict]:
                The created widget object.

        Examples:

            >>> tad.widgets.create(
            ...     dashboard_id=1,
            ...     pos_x=1,
            ...     pos_y=1,
            ...     width=2,
            ...     height=2,
            ...     title='ExampleWidget',
            ...     )
        '''
        payload = self._schema.dump(self._schema.load({
            'posX': pos_x,
            'posY': pos_y,
            'width': width,
            'height': height,
            'title': title
        }))

        return self._schema.load(self._post(f'{dashboard_id}/widgets', json=payload))

    def details(self,
                dashboard_id: str,
                widget_id: int) -> Dict:
        '''
        Retrieves the details for a specific widget.

        Args:
            dashboard_id: The dashboard instance identifier.
            widget_id: The widget instance identifier

        Returns:
            dict:
                the widget object.

        Examples:

            >>> tad.directories.details(1)
        '''
        return self._schema.load(self._get(f"{dashboard_id}/widgets/{widget_id}"))

    def update(self,
               dashboard_id: str,
               widget_id: int,
               **kwargs) -> Dict:
        '''
        update an existing widget

        Args:
            dashboard_id:
                The dashboard instance identifier.
            widget_id:
                The dashboard instance identifier.
            pos_x:
                x-axis position for widget.
            pos_y:
                y-axis position for widget.
            width:
                width of widget.
            height:
                height of widget.
            title:
                title for widget.


        Returns:
            dict:
                The updated widget object.

        Examples:

            >>> tad.widgets.update(
            ...     dashboard_id=1,
            ...     widget_id=1,
            ...     pos_x=1,
            ...     pos_y=1,
            ...     width=3,
            ...     height=3,
            ...     title='EditedWidget'
            ...     )
        '''
        payload = self._schema.dump(kwargs)
        return self._schema.load(self._api.patch(f"{self._path}/{dashboard_id}/widgets/{widget_id}", json=payload))

    def delete(self,
               dashboard_id: str,
               widget_id: int) -> None:
        '''
        delete an existing widget

        Args:
            dashboard_id:
                The dashboard instance identifier.
            widget_id:
                The dashboard instance identifier.


        Returns:
            None:

        Examples:

            >>> tad.widgets.delete(
            ...     dashboard_id=1,
            ...     widget_id=1
            ...     )
        '''
        self._api.delete(f"dashboards/{dashboard_id}/widgets/{widget_id}")

    def widget_options_details(self,
                               dashboard_id: str,
                               widget_id: int) -> Dict:
        '''
        get widget options

        Args:
            dashboard_id:
                The dashboard instance identifier.
            widget_id:
                The dashboard instance identifier.


        Returns:
            dict:
                The widget option object.

        Examples:

            >>> tad.widgets.widget_options_details(
            ...     widget_id=1,
            ...     dashboard_id=1
            ...     )
        '''
        schema = WidgetOptionSchema()
        return schema.load(self._get(f"{dashboard_id}/widgets/{widget_id}/options"))

    def define_widget_options(self,
                              dashboard_id: str,
                              widget_id: str,
                              chart_type: str,
                              series: List[Dict]
                              ) -> None:
        '''
        Define a widget option

        Args:
            dashboard_id:
                The dashboard instance identifier.
            widget_id:
               The dashboard instance identifier.
            chart_type:
                The type of chart for widget. possible options are ``BigNumber``, ``LineChart``
                ``BarChart``, ``SecurityCompliance`` and ``StepChart``.
            series:
                Additional keywords passed will be added to the series list of dicts
                within the API call.


       Returns:
           None

       Examples:

            >>> tad.widgets.define_widget_options(
            ...     dashboard_id=1,
            ...     widget_id=1,
            ...     chart_type='BigNumber'
            ...     series=[
            ...     {
            ...         'dataOptions': {
            ...             'type': 'User',
            ...             'duration': 1,
            ...             'directoryIds': [1, 2, 3],
            ...             'active': True
            ...         },
            ...         'displayOptions': {
            ...             'label': 'label'
            ...         }
            ...     }
            ...     )
       '''
        schema = WidgetOptionSchema()
        payload = schema.dump(schema.load({
            'type': chart_type,
            'series': list(series)
        }))

        return self._schema.load(self._api.put(f"dashboards/{dashboard_id}/widgets/{widget_id}/options", json=payload))